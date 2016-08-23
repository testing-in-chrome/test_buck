/*
 * lib.cc
 *
 *  Created on: Aug 22, 2016
 *      Author: test
 */

#include "lib/lib.h"

#define GET_NAME(name) #name

namespace lib {

std::unique_ptr<std::string> GetName() {
  return std::make_unique<std::string>("Chrome Tester " GET_NAME("wow"));
}

}  // namespace lib
