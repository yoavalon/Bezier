d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
