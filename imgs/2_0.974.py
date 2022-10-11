d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(0,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)

d.end()
