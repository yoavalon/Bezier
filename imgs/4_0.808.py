d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)

d.end()
