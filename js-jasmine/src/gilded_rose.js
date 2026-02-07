class Item {
  constructor(name, sellIn, quality) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}

class Shop {
  constructor(items = []) {
    this.items = items;
  }

  updateQuality() {
    for (var i = 0; i < this.items.length; i++) {

      const item = this.items[i];

      if (item.name.startsWith("Conjured")) {
        updateConjuredItem(item);
      }
      else if (item.name.startsWith("Sulfuras")) {
        updateSulfuras(item);
      }
      else {
          switch (item.name) {
            case "Aged Brie":
              updateAgedBrie(item);
              break;

            case "Backstage passes to a TAFKAL80ETC concert":
              updateBackstagePass(item);
              break;

            default:
              updateNormalItem(item);
              break;
          }
      }
    }

    return this.items;
  }
}

function updateNormalItem(item) {
  item.sellIn = item.sellIn - 1;

  if (item.sellIn >= 0) {
    item.quality = item.quality - 1;
  } 
    else {
      item.quality = item.quality - 2;
    }

  if (item.quality < 0) {
    item.quality = 0;
  }
}

function updateAgedBrie(item) {
  item.sellIn = item.sellIn - 1;

  if (item.sellIn >= 0) {
    item.quality = item.quality + 1;
  } 
    else {
      item.quality = item.quality + 2;
    }

  if (item.quality > 50){
    item.quality = 50;
  } 
}

function updateBackstagePass(item) {
  item.sellIn = item.sellIn - 1;

  if (item.sellIn < 0) {
    item.quality = 0;
  } 
    else {
      item.quality = item.quality + 1;

      if (item.sellIn <= 10) {
        item.quality = item.quality + 1;
      }
      if (item.sellIn <= 5) {
        item.quality = item.quality + 1;
      }
    }

  if (item.quality > 50){
      item.quality = 50;
  } 
}

function updateSulfuras(item) {
  item.quality = 80;
}

function updateConjuredItem(item) {
  item.sellIn = item.sellIn - 1;

  if (item.sellIn >= 0) {
    item.quality = item.quality - 2;
  } 
    else {
      item.quality = item.quality - 4;
    }

  if (item.quality < 0) item.quality = 0;
}

module.exports = {
  Item,
  Shop,
};

