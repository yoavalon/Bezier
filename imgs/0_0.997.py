d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
