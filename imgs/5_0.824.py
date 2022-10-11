d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.short)
d.position_pen(1,1)

d.end()
