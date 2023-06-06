#include <cmath>
#include <vector>

#include <delaunator.hpp>

int main() {
  auto coords = std::vector<double> {-1, 1, 1, 1, 1, -1, -1, -1};
  auto d = delaunator::Delaunator(coords);
  return std::fabs(8.0 - d.get_hull_area()) < 0.001 ? 0 : 1;
}
