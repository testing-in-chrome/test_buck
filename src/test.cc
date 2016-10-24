// Copyright 2016 test

#include "gtest/include/gtest/gtest.h"
#include "lib/lib.h"

TEST(TestLib, Basic1) {
  EXPECT_EQ("Chrome Tester 3 \"wow\"", *lib::GetName());
}

TEST(TestLib, Basic2) {
  ASSERT_TRUE(lib::GetName());
}
