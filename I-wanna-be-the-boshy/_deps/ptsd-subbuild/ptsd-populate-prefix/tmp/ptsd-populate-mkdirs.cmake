# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file LICENSE.rst or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION ${CMAKE_VERSION}) # this file comes with cmake

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "C:/develop/I-wanna-be-the-boshy/PTSD")
  file(MAKE_DIRECTORY "C:/develop/I-wanna-be-the-boshy/PTSD")
endif()
file(MAKE_DIRECTORY
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-build"
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix"
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/tmp"
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/src/ptsd-populate-stamp"
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/src"
  "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/src/ptsd-populate-stamp"
)

set(configSubDirs Debug)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/src/ptsd-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/develop/I-wanna-be-the-boshy/_deps/ptsd-subbuild/ptsd-populate-prefix/src/ptsd-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
