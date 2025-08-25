export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Return a new instance of the same class as the current object
    return new this.constructor();
  }
}
