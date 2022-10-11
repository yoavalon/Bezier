d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,0)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
