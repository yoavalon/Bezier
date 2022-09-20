d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(3,3)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
