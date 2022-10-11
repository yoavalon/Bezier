d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.long)

d.end()
