d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.long)

d.end()
