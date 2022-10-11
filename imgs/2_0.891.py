d = DslBezier()

d.position_pen(3,2)
d.position_pen(2,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)

d.end()
