-- creates a trigger that decreases quantity of item
DELIMITER //
CREATE TRIGGER decrease_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
