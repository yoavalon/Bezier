d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)

d.end()
