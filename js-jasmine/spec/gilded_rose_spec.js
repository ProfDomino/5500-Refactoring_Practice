var { Shop, Item } = require("../src/gilded_rose.js");

describe("Gilded Rose", function () {
  it("Normal item decreases quality by 1", function () {
    const shop = new Shop([new Item("Normal Item", 10, 20)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(19);
  });

  it("Normal item decreases quality by 2 after sell by date", function () {
    const shop = new Shop([new Item("Normal Item", 0, 20)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(18);
  });

  it("Normal item quality never goes negative", function () {
    const shop = new Shop([new Item("Normal Item", 5, 0)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(0);
  });

  it("Aged Brie increases quality by 1", function () {
    const shop = new Shop([new Item("Aged Brie", 5, 10)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(11);
  });

  it("Aged Brie quality never exceeds 50", function () {
    const shop = new Shop([new Item("Aged Brie", 5, 50)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(50);
  });

  it("Sulfuras quality is always 80", function () {
    const shop = new Shop([new Item("Sulfuras", 0, 80)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(80);
  });

  it("Backstage pass increases quality by 2 when 10 days or less", function () {
    const shop = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
    ]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(22);
  });

  it("Backstage pass increases quality by 3 when 5 days or less", function () {
    const shop = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
    ]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(23);
  });

  it("Backstage pass quality drops to 0 after concert", function () {
    const shop = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 0, 50),
    ]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(0);
  });

  it("Conjured item decreases quality by 2", function () {
    const shop = new Shop([new Item("Conjured Mana Cake", 10, 20)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(18);
  });

  it("Conjured item decreases quality by 4 after sell by date", function () {
    const shop = new Shop([new Item("Conjured Mana Cake", 0, 20)]);
    shop.updateQuality();
    expect(shop.items[0].quality).toEqual(16);
  });
});
