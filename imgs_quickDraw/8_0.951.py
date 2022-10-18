d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)

d.end()
