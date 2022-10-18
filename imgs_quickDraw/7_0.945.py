d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.N, Length.medium)

d.end()
