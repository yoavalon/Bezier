d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)

d.end()
