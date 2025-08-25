export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Check if this is a subclass and if it has the required method
    if (this.constructor !== Building && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    // This is the method that must be overridden
  }
}
