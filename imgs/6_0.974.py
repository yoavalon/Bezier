d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
