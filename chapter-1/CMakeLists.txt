file(GLOB dirs "exercise-*")
foreach(dir ${dirs})
        add_subdirectory(${dir})
endforeach()
