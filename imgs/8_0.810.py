d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
