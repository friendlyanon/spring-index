#include <cstddef>

#include <smmalloc/smmalloc.h>

namespace {

constexpr std::uint32_t bucket_count = 1;
constexpr std::size_t int_size = sizeof(int);

constexpr std::size_t int_align = alignof(int);

}

int main() {
  sm_allocator space = _sm_allocator_create(bucket_count, int_size);
  if (space == nullptr) {
    return 1;
  }

  void* p = _sm_malloc(space, int_size, int_align);
  if (p == nullptr) {
    return 2;
  }

  int* x = new (p) int(0);
  int value = *x;

  using T = int;
  x->~T();

  _sm_free(space, p);
  _sm_allocator_destroy(space);

  return value == 0 ? 0 : 3;
}
