d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)

d.end()
