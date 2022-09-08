d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,2)

d.end()
