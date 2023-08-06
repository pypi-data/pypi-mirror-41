#version 450
#include "Pluto/Resources/Shaders/ShaderCommon.hxx"

layout(location = 0) in vec3 point;
layout(location = 1) in vec4 color;
layout(location = 2) in vec3 normal;
layout(location = 3) in vec2 texcoord;

layout(location = 0) out vec4 fragColor;

out gl_PerVertex {
    vec4 gl_Position;
    float gl_PointSize;
};

void main() {
    EntityStruct target_entity = ebo.entities[push.consts.target_id];
    EntityStruct camera_entity = ebo.entities[push.consts.camera_id];
    
    CameraStruct camera = cbo.cameras[camera_entity.camera_id];
    TransformStruct camera_transform = tbo.transforms[camera_entity.transform_id];

    TransformStruct target_transform = tbo.transforms[target_entity.transform_id];

    vec3 w_position = vec3(target_transform.localToWorld * vec4(point.xyz, 1.0));
    #ifdef DISABLE_MULTIVIEW
    int viewIndex = push.consts.viewIndex;
    #else
    int viewIndex = gl_ViewIndex;
    #endif
    gl_Position = camera.multiviews[viewIndex].proj * camera.multiviews[viewIndex].view * camera_transform.worldToLocal * vec4(w_position, 1.0);
    gl_PointSize = 1.0;
    fragColor = vec4(normalize(normal), 1.0f);
}
