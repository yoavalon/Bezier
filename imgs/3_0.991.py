d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)

d.end()
