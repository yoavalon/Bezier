d = DslBezier()

d.position_pen(2,3)
d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)

d.end()
