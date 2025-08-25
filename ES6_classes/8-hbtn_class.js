export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  // Called when casting to Number
  valueOf() {
    return this._size;
  }

  // Called when casting to String
  toString() {
    return this._location;
  }
}
