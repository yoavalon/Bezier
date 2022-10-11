d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)

d.end()
