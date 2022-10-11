d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,0)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)

d.end()
