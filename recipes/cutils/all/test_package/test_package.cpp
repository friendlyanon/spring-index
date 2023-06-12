#include <cmath>
#include <vector>

#include <CUtils/Util.h>

int main() {
  return util_isWhiteSpace(' ') && !util_isWhiteSpace('a') ? 0 : 1;
}
