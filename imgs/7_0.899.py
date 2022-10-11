d = DslBezier()

d.position_pen(0,1)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
