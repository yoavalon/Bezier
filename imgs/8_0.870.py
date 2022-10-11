d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,1)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)

d.end()
