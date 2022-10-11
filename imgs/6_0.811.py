d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(2,0)

d.end()
