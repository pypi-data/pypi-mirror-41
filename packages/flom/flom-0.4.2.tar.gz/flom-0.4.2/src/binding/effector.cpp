//
// Copyright 2018 coord.e
//
// This file is part of flom-py.
//
// flom-py is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// flom-py is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with flom-py.  If not, see <http://www.gnu.org/licenses/>.
//

#include <flom/effector.hpp>

#include <pybind11/eigen.h>
#include <pybind11/numpy.h>
#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "declarations.hpp"
#include "optional_caster.hpp"

namespace flom_py {

namespace py = pybind11;

void define_effector(py::module &m) {
  py::class_<flom::EffectorDifference>(m, "EffectorDifference")
      .def(py::init<const flom::Effector &, const flom::Effector &>())
      .def(py::init<const flom::EffectorDifference &>())
      .def_property_readonly(
          "location",
          [](const flom::EffectorDifference &eff) { return eff.location(); })
      .def_property_readonly(
          "rotation",
          [](const flom::EffectorDifference &eff) { return eff.rotation(); })
      .def("is_compatible", &flom::EffectorDifference::is_compatible)
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def(py::self + py::self)
      .def(py::self += py::self)
      .def(py::self * std::size_t())
      .def(py::self *= std::size_t());

  py::class_<flom::Effector>(m, "Effector")
      .def(py::init<>())
      .def(py::init<const flom::compat::optional<flom::Location> &,
                    const flom::compat::optional<flom::Rotation> &>())
      .def(py::init<const flom::Effector &>())
      .def_property("location",
                    [](const flom::Effector &eff) { return eff.location(); },
                    &flom::Effector::set_location)
      .def_property("rotation",
                    [](const flom::Effector &eff) { return eff.rotation(); },
                    &flom::Effector::set_rotation)
      .def("clear_location", &flom::Effector::clear_location)
      .def("clear_rotation", &flom::Effector::clear_rotation)
      .def("new_compatible_effector", &flom::Effector::new_compatible_effector)
      .def("is_compatible", py::overload_cast<const flom::Effector &>(
                                &flom::Effector::is_compatible, py::const_))
      .def("is_compatible", py::overload_cast<const flom::EffectorDifference &>(
                                &flom::Effector::is_compatible, py::const_))
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def(py::self - py::self)
      .def("__add__",
           [](const flom::Effector &e, const flom::EffectorDifference &diff) {
             return e + diff;
           })
      .def("__iadd__",
           [](flom::Effector &e, const flom::EffectorDifference &diff) {
             return e += diff;
           });

  py::class_<flom::Location>(m, "Location")
      .def(py::init<>())
      .def(py::init<double, double, double>(), py::arg("x"), py::arg("y"),
           py::arg("z"))
      .def(py::init<const flom::Location::value_type &>())
      .def(py::init<const flom::Location &>())
      .def_property("vector", &flom::Location::vector,
                    &flom::Location::set_vector,
                    py::return_value_policy::reference_internal)
      .def_property("x", &flom::Location::x, &flom::Location::set_x)
      .def_property("y", &flom::Location::y, &flom::Location::set_y)
      .def_property("z", &flom::Location::z, &flom::Location::set_z)
      .def("xyz", &flom::Location::xyz)
      .def("set_xyz", &flom::Location::set_xyz)
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def(py::self + py::self)
      .def(py::self += py::self)
      .def(py::self - py::self)
      .def(py::self -= py::self)
      .def(py::self * std::size_t())
      .def(py::self *= std::size_t());

  py::class_<flom::Rotation>(m, "Rotation")
      .def(py::init<>())
      .def(py::init<double, double, double, double>(), py::arg("w"),
           py::arg("x"), py::arg("y"), py::arg("z"))
      .def(py::init([](const Eigen::Vector4d &coeffs) {
        return flom::Rotation{Eigen::Quaternion<double>(coeffs)};
      }))
      .def(py::init<const flom::Rotation &>())
      .def_property(
          "quaternion",
          [](const flom::Rotation &rot) { return rot.quaternion().coeffs(); },
          [](flom::Rotation &rot, const Eigen::Vector4d &coeffs) {
            rot.set_quaternion(Eigen::Quaternion<double>(coeffs));
          },
          py::return_value_policy::reference_internal)
      .def_property_readonly("w", &flom::Rotation::w)
      .def_property_readonly("x", &flom::Rotation::x)
      .def_property_readonly("y", &flom::Rotation::y)
      .def_property_readonly("z", &flom::Rotation::z)
      .def("wxyz", &flom::Rotation::wxyz)
      .def("set_wxyz", &flom::Rotation::set_wxyz)
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def(py::self + py::self)
      .def(py::self += py::self)
      .def(py::self - py::self)
      .def(py::self -= py::self)
      .def(py::self * std::size_t())
      .def(py::self *= std::size_t());
}

} // namespace flom_py
