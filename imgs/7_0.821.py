d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
