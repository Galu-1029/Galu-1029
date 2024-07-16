cmake_minimum_required(VERSION 3.16)
project(yaskawa_gp7_support)

find_package(ament_cmake REQUIRED)
install(
	DIRECTORY config launch meshes urdf
	DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})

if(BUILD_TESTING)

endif()

ament_package()
