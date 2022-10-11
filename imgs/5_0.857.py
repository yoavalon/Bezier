d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.position_pen(1,0)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.medium)

d.end()
