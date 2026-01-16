cmake_minimum_required(VERSION 3.14)
project(VehicleDataService)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Compiler warnings for MISRA compliance
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-Wall -Wextra -Werror -pedantic)
endif()

# Main service library
add_library(vehicle_data_service
    VehicleDataService.cpp
)

target_include_directories(vehicle_data_service PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Standalone demo executable
add_executable(vehicle_data_demo
    VehicleDataService.cpp
)

target_compile_definitions(vehicle_data_demo PRIVATE STANDALONE_DEMO)

# Installation
install(TARGETS vehicle_data_service
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES VehicleDataService.cpp
    DESTINATION include/sdv/services
)
