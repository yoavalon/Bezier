d = DslBezier()

d.position_pen(2,1)
d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)

d.end()
