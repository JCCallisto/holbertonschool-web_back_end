export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Use Symbol.species to get the correct constructor
    const Species = this.constructor[Symbol.species] || this.constructor;
    return new Species();
  }
}

// Define Symbol.species for the Car class
Car[Symbol.species] = Car;
