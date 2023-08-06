#version 450
#include "Pluto/Resources/Shaders/ShaderCommon.hxx"
#include "Pluto/Resources/Shaders/VertexCommon.hxx"

void main() {
    EntityStruct target_entity = ebo.entities[push.consts.target_id];
    EntityStruct camera_entity = ebo.entities[push.consts.camera_id];
    
    CameraStruct camera = cbo.cameras[camera_entity.camera_id];
    
    TransformStruct camera_transform = tbo.transforms[camera_entity.transform_id];
    TransformStruct target_transform = tbo.transforms[target_entity.transform_id];

    w_position = vec3(target_transform.localToWorld * vec4(point.xyz, 1.0));
    w_normal = normalize(transpose(target_transform.worldToLocal) * vec4(normal, 0.0)).xyz;
    #ifdef DISABLE_MULTIVIEW
    int viewIndex = push.consts.viewIndex;
    #else
    int viewIndex = gl_ViewIndex;
    #endif
    w_cameraPos = vec3(camera.multiviews[viewIndex].viewinv[3]) + vec3(camera_transform.localToWorld[3]);

    fragTexCoord = texcoord;
    gl_Position = camera.multiviews[viewIndex].proj * camera.multiviews[viewIndex].view * camera_transform.worldToLocal * vec4(w_position, 1.0);

    m_position = point;
    s_position = gl_Position.xyz / gl_Position.w;
    vert_color = color;
}
