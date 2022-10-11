d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)

d.end()
