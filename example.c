#include "example.h"

int prime(int n) {
  int i;
  for (i = 2; i < n; i++) {
    if (n % i == 0) {
      return 0;
    }
  }
  return 1;
}

int odd_even(int n) {
  if (n % 2 == 0) {
    return 0;
  }
  return 1;
}