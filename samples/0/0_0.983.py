d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.NW, Length.medium)

d.end()
