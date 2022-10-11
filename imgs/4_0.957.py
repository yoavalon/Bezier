d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.long)
d.position_pen(3,1)

d.end()
