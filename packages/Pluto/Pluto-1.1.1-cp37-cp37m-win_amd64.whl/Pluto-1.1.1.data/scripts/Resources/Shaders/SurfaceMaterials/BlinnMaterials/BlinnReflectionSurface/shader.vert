#version 450
#extension GL_ARB_separate_shader_objects : enable

layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec3 inNormal;

layout(location = 0) out vec3 normal;
layout(location = 1) out vec3 position;
layout(location = 2) out vec3 outRefl;

layout(binding = 0) uniform CameraBufferObject {
    mat4 view;
    mat4 proj;
    mat4 viewinv;
    mat4 projinv;
    float near;
    float far;
} cbo;

layout(binding = 1) uniform UniformBufferObject {
  mat4 modelMatrix;
  mat4 normalMatrix;
  vec4 ka;
  vec4 kd;
  vec4 ks;
} ubo;

out gl_PerVertex {
    vec4 gl_Position;
    float gl_PointSize;
};

void main() {
  /* Compute vertex screen position */
    gl_Position = cbo.proj * cbo.view * ubo.modelMatrix * vec4(inPosition, 1.0);
  
    normal = vec3(ubo.normalMatrix * vec4(inNormal, 0));
    position = vec3(cbo.view * ubo.modelMatrix * vec4(inPosition, 1.0));

    vec3 w_vertPos = vec3(ubo.modelMatrix * vec4(inPosition.xyz, 1.0));
    vec3 w_cameraPos = vec3(cbo.viewinv[3]);
    vec3 w_viewDir = w_vertPos - w_cameraPos;

    vec3 w_norm = inNormal;
    vec3 w_reflection = reflect(w_viewDir, w_norm);
    
    /* From z up to y up */
    outRefl.x = w_reflection.x;
    outRefl.y = w_reflection.z;
    outRefl.z = w_reflection.y;
}