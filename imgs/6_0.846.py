d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.medium)

d.end()
