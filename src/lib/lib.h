/*
 * lib.h
 *
 *  Created on: Aug 22, 2016
 *      Author: test
 */

#ifndef SRC_LIB_LIB_H_
#define SRC_LIB_LIB_H_


#include <memory>
#include <string>

namespace lib {

std::unique_ptr<std::string> GetName();

}  // namespace lib

#endif /* SRC_LIB_LIB_H_ */
