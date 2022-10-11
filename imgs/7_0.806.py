d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(3,0)
d.straight_line(Direction.NW, Length.short)

d.end()
