set(P3PGRAPHNODES_HEADERS
    ambientLight.h ambientLight.I
    callbackNode.h callbackNode.I
    config_pgraphnodes.h
    directionalLight.h directionalLight.I
    fadeLodNode.I fadeLodNode.h fadeLodNodeData.h
    lightLensNode.h lightLensNode.I
    lightNode.h lightNode.I
    lodNode.I lodNode.h lodNodeType.h
    nodeCullCallbackData.h nodeCullCallbackData.I
    pointLight.h pointLight.I
    sceneGraphAnalyzer.h sceneGraphAnalyzer.I
    selectiveChildNode.h selectiveChildNode.I
    sequenceNode.h sequenceNode.I
    shaderGenerator.h shaderGenerator.I
    spotlight.h spotlight.I
    switchNode.h switchNode.I
    uvScrollNode.I uvScrollNode.h
)

set(P3PGRAPHNODES_SOURCES
    ambientLight.cxx
    callbackNode.cxx
    config_pgraphnodes.cxx
    directionalLight.cxx
    fadeLodNode.cxx fadeLodNodeData.cxx
    lightLensNode.cxx
    lightNode.cxx
    lodNode.cxx lodNodeType.cxx
    nodeCullCallbackData.cxx
    pointLight.cxx
    sceneGraphAnalyzer.cxx
    selectiveChildNode.cxx
    sequenceNode.cxx
    shaderGenerator.cxx
    spotlight.cxx
    switchNode.cxx
    uvScrollNode.cxx
)

composite_sources(p3pgraphnodes P3PGRAPHNODES_SOURCES)
add_library(p3pgraphnodes ${P3PGRAPHNODES_HEADERS} ${P3PGRAPHNODES_SOURCES})
target_link_libraries(p3pgraphnodes p3pgraph)
target_interrogate(p3pgraphnodes ALL)

install(TARGETS p3pgraphnodes DESTINATION lib)