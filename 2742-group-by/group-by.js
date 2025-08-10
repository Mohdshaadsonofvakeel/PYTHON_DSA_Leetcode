// Define as non-enumerable to avoid showing up in for...in
Object.defineProperty(Array.prototype, 'groupBy', {
  value: function (fn) {
    const groups = Object.create(null); // null-prototype avoids inherited key collisions

    for (const item of this) {
      const key = String(fn(item)); // ensure string keys as per constraint
      if (!groups[key]) groups[key] = [];
      groups[key].push(item);
    }

    return groups;
  },
  writable: true,
  configurable: true,
});
